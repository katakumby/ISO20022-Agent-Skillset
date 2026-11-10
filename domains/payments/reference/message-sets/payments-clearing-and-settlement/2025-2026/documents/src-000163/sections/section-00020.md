---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.8 StatusReasonInformation <StsRsnInf>", "2.4.3.8.2 Reason <Rsn>", "2.4.3.8.2.1 Code <Cd>"]
file_pages: [37]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.8.2.1 Code <Cd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 37 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 37

```text
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 37
Or}   Proprietary <Prtry> [1..1] Text 37
2.4.3.8.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 1233
2.4.3.8.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 1246
2.4.3.8.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max105Text" on page 1244
2.4.3.9  ChargesInformation <ChrgsInf>
Presence: [0..*]
Definition: Provides information on the charges related to the processing of the rejection of the
instruction.
Usage: This is passed on for information purposes only. Settlement of the charges will be done
separately.
ChargesInformation <ChrgsInf> contains the following Charges16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 37
   Agent <Agt> [1..1] ± 38
   Type <Tp> [0..1]  38
{Or     Code <Cd> [1..1] CodeSet 39
Or}     Proprietary <Prtry> [1..1] ± 39
2.4.3.9.1  Amount <Amt>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
37 March 2026
```

