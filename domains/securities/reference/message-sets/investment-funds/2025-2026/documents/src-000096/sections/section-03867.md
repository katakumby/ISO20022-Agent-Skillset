---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction", "66.1.42.2 CashSettlement3", "66.1.42.2.1 CashAccountDetails <CshAcctDtls>", "66.1.42.2.1.1 SettlementCurrency <SttlmCcy>"]
file_pages: [5156]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42.2.1.1 SettlementCurrency <SttlmCcy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5156 to 5156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5156

```text
CashAccountDetails <CshAcctDtls> contains the following CashAccount204 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementCurrency <SttlmCcy> [1..1] CodeSet C1 5156
   Identification <Id> [1..1] ± 5156
   AccountOwner <AcctOwnr> [0..1] ± 5157
   AccountServicer <AcctSvcr> [0..1] ± 5157
   AccountServicerBranch <AcctSvcrBrnch> [0..1] ± 5157
   AccountOwnerOtherIdentification <AcctOwnrOthrId> [0..*] ± 5158
   InvestmentAccountType <InvstmtAcctTp> [0..1] ± 5158
   CreditDebit <CdtDbt> [0..1] CodeSet 5158
   SettlementInstructionReason <SttlmInstrRsn> [0..1]  5159
{Or     Code <Cd> [1..1] CodeSet 5159
Or}     Proprietary <Prtry> [1..1] ± 5160
   CashAccountPurpose <CshAcctPurp> [0..1]  5160
{Or     Code <Cd> [1..1] CodeSet 5160
Or}     Proprietary <Prtry> [1..1] ± 5160
   CashAccountDesignation <CshAcctDsgnt> [0..1]  5161
{Or     Code <Cd> [1..1] CodeSet 5161
Or}     Proprietary <Prtry> [1..1] ± 5161
   DividendPercentage <DvddPctg> [0..1] Rate 5161
66.1.42.2.1.1  SettlementCurrency <SttlmCcy>
Presence: [1..1]
Definition: Currency associated with the payment instrument.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.42.2.1.2  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5156 May 2026
```

