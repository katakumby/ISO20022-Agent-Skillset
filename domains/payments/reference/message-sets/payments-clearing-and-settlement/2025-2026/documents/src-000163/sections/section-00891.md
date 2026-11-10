---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.10 Mandate"]
file_pages: [1186]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.10 Mandate

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1186 to 1186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1186

```text
10.1.10 Mandate
10.1.10.1  MandateClassification1Choice
Definition: Specifies the high level purpose of the instruction based on a set of pre-defined categories.
Usage: This is used by the initiating party to provide information concerning the processing of the
payment. It is likely to trigger special processing by any of the agents involved in the payment chain.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1186
Or}   Proprietary <Prtry> [1..1] Text 1186
10.1.10.1.1  Code <Cd>
Presence: [1..1]
Definition: Category purpose, as published in an external category purpose code list.
Datatype: "MandateClassification1Code" on page 1234
CodeName Name Definition
FIXE Fixed Direct debit amount is fixed.
USGB UsageBased Direct debit amount is based on usage.
VARI Variable Direct debit amount is variable.
10.1.10.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 1246
10.1.10.2  MandateTypeInformation2
Definition: Set of elements used to further detail the information related to the type of payment.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1186 March 2026
```

