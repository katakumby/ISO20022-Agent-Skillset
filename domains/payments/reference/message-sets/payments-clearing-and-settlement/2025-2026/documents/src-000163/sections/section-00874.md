---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.5 Date Time", "10.1.5.1 DateAndDateTime2Choice", "10.1.5.1.1 Date <Dt>"]
file_pages: [1169]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.5.1.1 Date <Dt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1169 to 1169.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1169

```text
10.1.5.1.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 1239
10.1.5.1.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 1239
10.1.6 Direct Debit
10.1.6.1  CreditTransferMandateData1
Definition: Provides further details related to a credit transfer mandate signed between the creditor and
the debtor.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 1169
   Type <Tp> [0..1] ± 1169
   DateOfSignature <DtOfSgntr> [0..1] Date 1170
   DateOfVerification <DtOfVrfctn> [0..1] DateTime 1170
   ElectronicSignature <ElctrncSgntr> [0..1] Binary 1170
   FirstPaymentDate <FrstPmtDt> [0..1] Date 1170
   FinalPaymentDate <FnlPmtDt> [0..1] Date 1170
   Frequency <Frqcy> [0..1] ± 1171
   Reason <Rsn> [0..1]  1171
{Or     Code <Cd> [1..1] CodeSet 1171
Or}     Proprietary <Prtry> [1..1] Text 1171
10.1.6.1.1  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the mandate.
Datatype: "Max35Text" on page 1246
10.1.6.1.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of mandate, such as paper, electronic or scheme.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1169 March 2026
```

