---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.6 Direct Debit", "6.1.6.1 CreditTransferMandateData1", "6.1.6.1.3 DateOfSignature <DtOfSgntr>"]
file_pages: [536]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.6.1.3 DateOfSignature <DtOfSgntr>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 536 to 536.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 536

```text
Type <Tp> contains the following elements (see "MandateTypeInformation2" on page 550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ServiceLevel <SvcLvl> [0..1]  550
{Or     Code <Cd> [1..1] CodeSet 550
Or}     Proprietary <Prtry> [1..1] Text 550
   LocalInstrument <LclInstrm> [0..1]  550
{Or     Code <Cd> [1..1] CodeSet 551
Or}     Proprietary <Prtry> [1..1] Text 551
   CategoryPurpose <CtgyPurp> [0..1]  551
{Or     Code <Cd> [1..1] CodeSet 551
Or}     Proprietary <Prtry> [1..1] Text 551
   Classification <Clssfctn> [0..1] ± 551
6.1.6.1.3  DateOfSignature <DtOfSgntr>
Presence: [0..1]
Definition: Date on which the credit transfer mandate has been signed by the debtor.
Datatype: "ISODate" on page 603
6.1.6.1.4  DateOfVerification <DtOfVrfctn>
Presence: [0..1]
Definition: Date on which the credit transfer mandate has been verified.
Datatype: "ISODateTime" on page 603
6.1.6.1.5  ElectronicSignature <ElctrncSgntr>
Presence: [0..1]
Definition: Additional security provisions, such as a digital signature, as provided by the debtor.
Datatype: "Max10KBinary" on page 586
6.1.6.1.6  FirstPaymentDate <FrstPmtDt>
Presence: [0..1]
Definition: Date of the first payment of a recurrent credit transfer as per the mandate.
Datatype: "ISODate" on page 603
6.1.6.1.7  FinalPaymentDate <FnlPmtDt>
Presence: [0..1]
Definition: Date of the final payment of a recurrent credit transfer as per the mandate.
Datatype: "ISODate" on page 603
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 536 March 2026
```

