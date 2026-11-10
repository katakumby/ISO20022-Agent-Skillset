---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.2 StatementOfInvestmentFundTransactions2", "66.1.5.2.3 TransactionOnAccount <TxOnAcct>", "66.1.5.2.3.1 Identification <Id>"]
file_pages: [4351]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.2.3.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4351 to 4351.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4351

```text
TransactionOnAccount <TxOnAcct> contains the following InvestmentFundTransactionsByFund2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4351
   Name <Nm> [0..1] Text 4352
   SupplementaryIdentification <SplmtryId> [0..1] Text 4352
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4352
   ClassType <ClssTp> [0..1] Text 4352
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4352
   TransactionDetails <TxDtls> [1..*] ± C9, C10 4352
   BalanceByPage <BalByPg> [0..1] ± 4354
66.1.5.2.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security by an ISIN.
Identification <Id> contains one of the following elements (see "SecurityIdentification3Choice" on
page 5139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 5139
Or   SEDOL <SEDOL> [1..1] IdentifierSet 5139
Or   CUSIP <CUSIP> [1..1] IdentifierSet 5140
Or   RIC <RIC> [1..1] IdentifierSet 5140
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 5140
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 5140
Or   CTA <CTA> [1..1] IdentifierSet 5140
Or   QUICK <QUICK> [1..1] IdentifierSet 5140
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 5140
Or   Dutch <Dtch> [1..1] IdentifierSet 5141
Or   Valoren <Vlrn> [1..1] IdentifierSet 5141
Or   Sicovam <SCVM> [1..1] IdentifierSet 5141
Or   Belgian <Belgn> [1..1] IdentifierSet 5141
Or   Common <Cmon> [1..1] IdentifierSet 5141
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1] ± 5141
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4351 May 2026
```

