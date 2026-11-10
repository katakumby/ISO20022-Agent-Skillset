---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.7 GarnishmentRemittance <GrnshmtRmt>", "4.4.2.14.18.2.15.2.7.1 Type <Tp>", "4.4.2.14.18.2.15.2.7.1.1 CodeOrProprietary <CdOrPrtry>", "4.4.2.14.18.2.15.2.7.1.1.1 Code <Cd>"]
file_pages: [721]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.7.1.1.1 Code <Cd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 721 to 721.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 721

```text
4.4.2.14.18.2.15.2.7.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Garnishment type in a coded form.
Would suggest this to be an External Code List to contain:
GNCS    Garnishment from a third party payer for Child Support
GNDP    Garnishment from a Direct Payer for Child Support
GTPP     Garnishment from a third party payer to taxing agency.
Datatype: "ExternalGarnishmentType1Code" on page 898
4.4.2.14.18.2.15.2.7.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of garnishment.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.15.2.7.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the garnishment type.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.15.2.7.2  Garnishee <Grnshee>
Presence: [0..1]
Definition: Ultimate party that owes an amount of money to the (ultimate) creditor, in this case, to the
garnisher.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
721 March 2026
```

