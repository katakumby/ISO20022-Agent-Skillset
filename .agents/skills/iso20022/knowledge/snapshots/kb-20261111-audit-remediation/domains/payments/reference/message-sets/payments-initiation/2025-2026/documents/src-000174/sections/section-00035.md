---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.7 ChequeInstruction <ChqInstr>", "2.4.2.19.7.7 ChequeMaturityDate <ChqMtrtyDt>"]
file_pages: [61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.7.7 ChequeMaturityDate <ChqMtrtyDt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 61 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 61

```text
CodeName Name Definition
HIGH High Priority level is high.
NORM Normal Priority level is normal.
2.4.2.19.7.7  ChequeMaturityDate <ChqMtrtyDt>
Presence: [0..1]
Definition: Date when the draft becomes payable and the debtor's account is debited.
Datatype: "ISODate" on page 603
2.4.2.19.7.8  FormsCode <FrmsCd>
Presence: [0..1]
Definition: Identifies, in a coded form, the cheque layout, company logo and digitised signature to be
used to print the cheque, as agreed between the initiating party and the debtor's agent.
Datatype: "Max35Text" on page 609
2.4.2.19.7.9  MemoField <MemoFld>
Presence: [0..2]
Definition: Information that needs to be printed on a cheque, used by the payer to add miscellaneous
information.
Datatype: "Max35Text" on page 609
2.4.2.19.7.10  RegionalClearingZone <RgnlClrZone>
Presence: [0..1]
Definition: Regional area in which the cheque can be cleared, when a country has no nation-wide
cheque clearing organisation.
Datatype: "Max35Text" on page 609
2.4.2.19.7.11  PrintLocation <PrtLctn>
Presence: [0..1]
Definition: Specifies the print location of the cheque.
Datatype: "Max35Text" on page 609
2.4.2.19.7.12  Signature <Sgntr>
Presence: [0..5]
Definition: Signature to be used by the cheque servicer on a specific cheque to be printed.
Datatype: "Max70Text" on page 610
2.4.2.19.8  UltimateDebtor <UltmtDbtr>
Presence: [0..1]
Definition: Ultimate party that owes an amount of money to the (ultimate) creditor.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 61 March 2026
```

