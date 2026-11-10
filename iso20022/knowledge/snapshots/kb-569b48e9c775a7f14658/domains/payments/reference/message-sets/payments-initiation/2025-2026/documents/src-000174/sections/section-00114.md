---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.6 StatusReasonInformation <StsRsnInf>", "3.4.3.7.6.2 Reason <Rsn>", "3.4.3.7.6.2.1 Code <Cd>"]
file_pages: [175]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.6.2.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 175 to 175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 175

```text
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 175
Or}   Proprietary <Prtry> [1..1] Text 175
3.4.3.7.6.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 597
3.4.3.7.6.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 609
3.4.3.7.6.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max105Text" on page 607
3.4.3.7.7  ChargesInformation <ChrgsInf>
Presence: [0..*]
Definition: Provides information on the charges related to the processing of the rejection of the
instruction.
Usage: This is passed on for information purposes only. Settlement of the charges will be done
separately.
ChargesInformation <ChrgsInf> contains the following Charges16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 175
   Agent <Agt> [1..1] ± 176
   Type <Tp> [0..1]  176
{Or     Code <Cd> [1..1] CodeSet 177
Or}     Proprietary <Prtry> [1..1] ± 177
3.4.3.7.7.1  Amount <Amt>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 175 March 2026
```

