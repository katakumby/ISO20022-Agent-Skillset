---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.5 Date Time", "6.1.5.1 DateAndDateTime2Choice", "6.1.5.1.1 Date <Dt>"]
file_pages: [535]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.5.1.1 Date <Dt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 535 to 535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 535

```text
6.1.5.1.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 603
6.1.5.1.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 603
6.1.6 Direct Debit
6.1.6.1  CreditTransferMandateData1
Definition: Provides further details related to a credit transfer mandate signed between the creditor and
the debtor.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 535
   Type <Tp> [0..1] ± 535
   DateOfSignature <DtOfSgntr> [0..1] Date 536
   DateOfVerification <DtOfVrfctn> [0..1] DateTime 536
   ElectronicSignature <ElctrncSgntr> [0..1] Binary 536
   FirstPaymentDate <FrstPmtDt> [0..1] Date 536
   FinalPaymentDate <FnlPmtDt> [0..1] Date 536
   Frequency <Frqcy> [0..1] ± 537
   Reason <Rsn> [0..1]  537
{Or     Code <Cd> [1..1] CodeSet 537
Or}     Proprietary <Prtry> [1..1] Text 537
6.1.6.1.1  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the mandate.
Datatype: "Max35Text" on page 609
6.1.6.1.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of mandate, such as paper, electronic or scheme.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 535 March 2026
```

