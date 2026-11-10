---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.9 CorporateActionConfirmationDetails <CorpActnConfDtls>", "9.4.9.4 CashMovementDetails <CshMvmntDtls>", "9.4.9.4.1 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [686]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.9.4.1 CreditDebitIndicator <CdtDbtInd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 686 to 686.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 686

```text
CashMovementDetails <CshMvmntDtls> contains the following CashOption109 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 686
   Account <Acct> [0..1]  686
{Or     CashAccount <CshAcct> [1..1] ± 686
Or     ChargesAccount <ChrgsAcct> [1..1] ± 687
Or}     TaxAccount <TaxAcct> [1..1] ± 687
   PostingDate <PstngDt> [1..1] ± 687
   OriginalPostingDate <OrgnlPstngDt> [0..1] ± 687
   ValueDate <ValDt> [0..1] Date 688
   PostingAmount <PstngAmt> [1..1] Amount C1, C6 688
9.4.9.4.1  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the value is a debit or credit.
Datatype: "CreditDebitCode" on page 1205
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
9.4.9.4.2  Account <Acct>
Presence: [0..1]
Definition: Choice between a cash account, a charges account or a tax account.
Account <Acct> contains one of the following Account10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CashAccount <CshAcct> [1..1] ± 686
Or   ChargesAccount <ChrgsAcct> [1..1] ± 687
Or}   TaxAccount <TaxAcct> [1..1] ± 687
9.4.9.4.2.1  CashAccount <CshAcct>
Presence: [1..1]
Definition: Account in which cash is maintained.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 686 February 2026
```

