import frappe
from frappe.utils import today, date_diff


def execute(filters=None):
    columns = get_columns()
    data = get_data()
    return columns, data


def get_columns():
    return [
        {
            "label": "Check List",
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Check List",
            "width": 160,
        },
        {
            "label": "Serial No",
            "fieldname": "hoist_serial_no",
            "fieldtype": "Data",
            "width": 140,
        },
        {
            "label": "Customer",
            "fieldname": "customer_name",
            "fieldtype": "Data",
            "width": 220,
        },
        {
            "label": "Region",
            "fieldname": "regions",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "Person",
            "fieldname": "contact_person",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "Branch",
            "fieldname": "name_of_person",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "City",
            "fieldname": "city",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "Check List Type",
            "fieldname": "check_list_type",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "Capacity",
            "fieldname": "capacity",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "Brand",
            "fieldname": "brand",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "Model",
            "fieldname": "item",
            "fieldtype": "Data",
            "width": 150,
        },
        {
            "label": "Year of Construction",
            "fieldname": "year_of_construction",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "1st Phase",
            "fieldname": "1_phase",
            "fieldtype": "Check",
            "width": 120,
        },
        {
            "label": "3rd Phase",
            "fieldname": "3_phase",
            "fieldtype": "Check",
            "width": 120,
        },
        {
            "label": "Speed",
            "fieldname": "speed",
            "fieldtype": "Data",
            "width": 120,
        },

        # -------------------- New Check List Fields --------------------

        {
            "label": "Small Service",
            "fieldname": "small_service",
            "fieldtype": "Check",
            "width": 120,
        },
        {
            "label": "Big Service",
            "fieldname": "big_service",
            "fieldtype": "Check",
            "width": 120,
        },
        {
            "label": "Hrs Reading",
            "fieldname": "hrs_reading",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "Ready Date",
            "fieldname": "ready_date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": "Next Due Date",
            "fieldname": "next_due_date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": "Problem",
            "fieldname": "problem",
            "fieldtype": "Small Text",
            "width": 250,
        },
        {
            "label": "Remarks",
            "fieldname": "remark1",
            "fieldtype": "Small Text",
            "width": 250,
        },
        {
            "label": "Received Date",
            "fieldname": "received_dt",
            "fieldtype": "Date",
            "width": 120,
        },

        # -------------------- Stock Entry --------------------

        {
            "label": "Stock Entry",
            "fieldname": "stock_entry",
            "fieldtype": "Link",
            "options": "Stock Entry",
            "width": 170,
        },
        {
            "label": "Stock Entry Date",
            "fieldname": "stock_entry_date",
            "fieldtype": "Date",
            "width": 150,
        },
        {
            "label": "STN Date",
            "fieldname": "stn_date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": "Received at YT",
            "fieldname": "received_at_yt",
            "fieldtype": "Date",
            "width": 130,
        },
        {
            "label": "CL Date",
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 130,
        },

        # -------------------- Quotation --------------------

        {
            "label": "Quotation",
            "fieldname": "quotation",
            "fieldtype": "Link",
            "options": "Quotation",
            "width": 170,
        },
        {
            "label": "Quotation Date",
            "fieldname": "quotation_date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": "Spare Amount",
            "fieldname": "spare_amount",
            "fieldtype": "Currency",
            "width": 150,
        },
        {
            "label": "Service Amount",
            "fieldname": "service_amount",
            "fieldtype": "Currency",
            "width": 150,
        },
        {
            "label": "Total Amount",
            "fieldname": "total_amount",
            "fieldtype": "Currency",
            "width": 150,
        },
        {
            "label": "Quotation Status",
            "fieldname": "quotation_status",
            "fieldtype": "Data",
            "width": 150,
        },

        # -------------------- Sales Order --------------------

        {
            "label": "PO No",
            "fieldname": "po_no",
            "fieldtype": "Data",
            "width": 140,
        },
        {
            "label": "PO Date",
            "fieldname": "po_date",
            "fieldtype": "Date",
            "width": 140,
        },
        {
            "label": "Sales Order No",
            "fieldname": "sales_order",
            "fieldtype": "Link",
            "options": "Sales Order",
            "width": 170,
        },
        {
            "label": "SO Date",
            "fieldname": "so_date",
            "fieldtype": "Date",
            "width": 120,
        },

        # -------------------- Delivery Note --------------------

        {
            "label": "Delivery Note",
            "fieldname": "delivery_note",
            "fieldtype": "Link",
            "options": "Delivery Note",
            "width": 170,
        },
        {
            "label": "Delivery Date",
            "fieldname": "delivery_date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": "Reached on Site Date",
            "fieldname": "reached_on_site_date",
            "fieldtype": "Date",
            "width": 150,
        },

        # -------------------- New Delivery Note Fields --------------------

        {
            "label": "Transport Receipt No",
            "fieldname": "lr_no",
            "fieldtype": "Data",
            "width": 160,
        },
        {
            "label": "Transport Receipt Date",
            "fieldname": "lr_date",
            "fieldtype": "Date",
            "width": 160,
        },

        # -------------------- Sales Invoice --------------------

        {
            "label": "Sales Invoice No",
            "fieldname": "sales_invoice",
            "fieldtype": "Link",
            "options": "Sales Invoice",
            "width": 170,
        },
        {
            "label": "Sales Invoice Date",
            "fieldname": "invoice_date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": "Next Due Days",
            "fieldname": "no_of_days",
            "fieldtype": "Int",
            "width": 110,
        },

        # -------------------- Date Difference Columns --------------------

        {
            "label": "CL-Received",
            "fieldname": "cl_received",
            "fieldtype": "Int",
            "width": 120,
        },
        {
            "label": "Qtn-CL",
            "fieldname": "qtn_cl",
            "fieldtype": "Int",
            "width": 120,
        },
        {
            "label": "PO-Qtn",
            "fieldname": "po_qtn",
            "fieldtype": "Int",
            "width": 120,
        },
        {
            "label": "SO-PO",
            "fieldname": "so_po",
            "fieldtype": "Int",
            "width": 120,
        },
        {
            "label": "DN-PO",
            "fieldname": "dn_po",
            "fieldtype": "Int",
            "width": 120,
        },
        {
            "label": "SINV-PO",
            "fieldname": "sinv_po",
            "fieldtype": "Int",
            "width": 120,
        },
        {
            "label": "Current Status",
            "fieldname": "current_status",
            "fieldtype": "Data",
            "width": 140,
        },
    ]


def get_data():
    data = []

    check_lists = frappe.get_all(
        "Check List",
        fields=[
            "name",
            "hoist_serial_no",
            "customer_name",
            "check_list_type",
            "stock_entry_id",
            "regions",
            "name_of_person",
            "capacity",
            "contact_person",
            "city",
            "date",
            "year_of_construction",
            "1_phase",
            "3_phase",
            "problem",
            "speed",
            "brand",
            "received_dt",
            "item",
            "ready_date",
            "remark1",
            "next_due_date",
            "small_service",
            "big_service",
            "hrs_reading",
        ]
    )

    for cl in check_lists:

        row = cl.copy()

        # -------------------- Next Due Days --------------------

        if cl.get("next_due_date"):
            row["no_of_days"] = date_diff(
                cl.get("next_due_date"),
                today()
            )
        else:
            row["no_of_days"] = None

        # -------------------- Stock Entry --------------------

        row["stock_entry"] = ""
        row["stock_entry_date"] = ""
        row["stn_date"] = ""
        row["received_at_yt"] = ""

        if cl.stock_entry_id:

            se = frappe.db.get_value(
                "Stock Entry",
                cl.stock_entry_id,
                [
                    "name",
                    "posting_date",
                    "custom_stn_date",
                    "custom_received_dt",
                ],
                as_dict=True
            )

            if se:
                row["stock_entry"] = se.name
                row["stock_entry_date"] = se.posting_date
                row["stn_date"] = se.custom_stn_date
                row["received_at_yt"] = se.custom_received_dt

        # -------------------- Quotation --------------------

        row["quotation"] = ""
        row["quotation_date"] = ""
        row["quotation_status"] = ""
        row["spare_amount"] = 0
        row["service_amount"] = 0
        row["total_amount"] = 0

        if row["stock_entry"]:

            quotation = frappe.db.get_value(
                "Quotation",
                {"custom_stock_entry": row["stock_entry"]},
                [
                    "name",
                    "transaction_date",
                    "status",
                ],
                as_dict=True
            )

            if quotation:
                row["quotation"] = quotation.name
                row["quotation_date"] = quotation.transaction_date
                row["quotation_status"] = quotation.status

        # -------------------- Sales Order --------------------

        row["sales_order"] = ""
        row["so_date"] = ""
        row["po_no"] = ""
        row["po_date"] = ""

        if row.get("quotation"):

            quotation_items = frappe.get_all(
                "Quotation Item",
                filters={"parent": row["quotation"]},
                fields=["name"]
            )

            if quotation_items:

                quotation_item_names = [
                    d.name for d in quotation_items
                ]

                so_item = frappe.get_all(
                    "Sales Order Item",
                    filters={
                        "quotation_item": [
                            "in",
                            quotation_item_names
                        ]
                    },
                    fields=["parent"],
                    limit=1
                )

                if so_item:

                    sales_order = frappe.db.get_value(
                        "Sales Order",
                        so_item[0].parent,
                        [
                            "name",
                            "transaction_date",
                            "po_no",
                            "po_date",
                        ],
                        as_dict=True
                    )

                    if sales_order:

                        row["sales_order"] = sales_order.name
                        row["so_date"] = sales_order.transaction_date
                        row["po_no"] = sales_order.po_no
                        row["po_date"] = sales_order.po_date

                        # -------------------- Service / Spare Amount --------------------

                        sales_order_items = frappe.get_all(
                            "Sales Order Item",
                            filters={
                                "parent": sales_order.name
                            },
                            fields=[
                                "amount",
                                "is_stock_item",
                            ]
                        )

                        spare_amount = 0
                        service_amount = 0

                        for item in sales_order_items:

                            if item.is_stock_item:
                                spare_amount += item.amount or 0
                            else:
                                service_amount += item.amount or 0

                        row["spare_amount"] = spare_amount
                        row["service_amount"] = service_amount
                        row["total_amount"] = (
                            spare_amount + service_amount
                        )

        # -------------------- Delivery Note --------------------

        row["delivery_note"] = ""
        row["delivery_date"] = ""
        row["reached_on_site_date"] = ""
        row["lr_no"] = ""
        row["lr_date"] = ""

        if row.get("sales_order"):

            delivery_note = frappe.db.get_value(
                "Delivery Note",
                {
                    "custom_so_no": row["sales_order"]
                },
                [
                    "name",
                    "posting_date",
                    "custom_actual_delivery_date",
                    "custom_reached_on_site_date",
                    "lr_no",
                    "lr_date",
                ],
                as_dict=True,
            )

            if delivery_note:

                row["delivery_note"] = delivery_note.name
                row["delivery_date"] = delivery_note.posting_date

                # Reached on Site Date
                row["reached_on_site_date"] = (
                    delivery_note.custom_reached_on_site_date
                )

                row["lr_no"] = delivery_note.lr_no
                row["lr_date"] = delivery_note.lr_date

        # -------------------- Sales Invoice --------------------

        row["sales_invoice"] = ""
        row["invoice_date"] = ""

        if row["delivery_note"]:

            sales_invoice = frappe.db.get_value(
                "Sales Invoice",
                {
                    "custom_delivery_note_id": row["delivery_note"]
                },
                [
                    "name",
                    "posting_date",
                ],
                as_dict=True
            )

            if sales_invoice:
                row["sales_invoice"] = sales_invoice.name
                row["invoice_date"] = sales_invoice.posting_date

        # -------------------- Date Difference Calculations --------------------

        # CL-Received = CL Date - Received Date
        if row.get("date") and row.get("received_dt"):
            row["cl_received"] = date_diff(
                row["date"],
                row["received_dt"]
            )
        else:
            row["cl_received"] = None

        # Qtn-CL = Quotation Date - CL Date
        if row.get("quotation_date") and row.get("date"):
            row["qtn_cl"] = date_diff(
                row["quotation_date"],
                row["date"]
            )
        else:
            row["qtn_cl"] = None

        # PO-Qtn = PO Date - Quotation Date
        if row.get("po_date") and row.get("quotation_date"):
            row["po_qtn"] = date_diff(
                row["po_date"],
                row["quotation_date"]
            )
        else:
            row["po_qtn"] = None

        # SO-PO = SO Date - PO Date
        if row.get("so_date") and row.get("po_date"):
            row["so_po"] = date_diff(
                row["so_date"],
                row["po_date"]
            )
        else:
            row["so_po"] = None

        # DN-PO = Delivery Date - PO Date
        if row.get("delivery_date") and row.get("po_date"):
            row["dn_po"] = date_diff(
                row["delivery_date"],
                row["po_date"]
            )
        else:
            row["dn_po"] = None

        # SINV-PO = Sales Invoice Date - PO Date
        if row.get("invoice_date") and row.get("po_date"):
            row["sinv_po"] = date_diff(
                row["invoice_date"],
                row["po_date"]
            )
        else:
            row["sinv_po"] = None

        # -------------------- Current Status --------------------

        if row["sales_invoice"]:
            row["current_status"] = "Sales Invoice"

        elif row["delivery_note"]:
            row["current_status"] = "Delivery Note"

        elif row["sales_order"]:
            row["current_status"] = "Sales Order"

        elif row["quotation"]:
            row["current_status"] = "Quotation"

        elif row["stock_entry"]:
            row["current_status"] = "Stock Entry"

        else:
            row["current_status"] = "Check List"

        data.append(row)

    return data