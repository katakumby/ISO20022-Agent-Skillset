---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction", "66.1.42.1 CashSettlement4", "66.1.42.1.2 CashAccountDetails <CshAcctDtls>", "66.1.42.1.2.7 InvestmentAccountType <InvstmtAcctTp>"]
file_pages: [5150]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42.1.2.7 InvestmentAccountType <InvstmtAcctTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5150 to 5150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5150

```text
AccountOwnerOtherIdentification <AcctOwnrOthrId> contains the following elements (see
"GenericIdentification82" on page 4541 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4541
   Type <Tp> [1..1]  4541
{Or     Code <Cd> [1..1] CodeSet 4541
Or}     Proprietary <Prtry> [1..1] ± 4542
   Issuer <Issr> [0..1] Text 4543
   IssueDate <IsseDt> [0..1] Date 4543
   ExpiryDate <XpryDt> [0..1] Date 4543
   State <Stat> [0..1] Text 4543
   IssuerCountry <IssrCtry> [0..1] CodeSet C12 4543
66.1.42.1.2.7  InvestmentAccountType <InvstmtAcctTp>
Presence: [0..1]
Definition: Type of account.
InvestmentAccountType <InvstmtAcctTp> contains one of the following elements (see
"AccountType2Choice" on page 4327 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4327
Or}   Proprietary <Prtry> [1..1] ± 4327
66.1.42.1.2.8  CreditDebit <CdtDbt>
Presence: [0..1]
Definition: Specifies if the account is for credits or debits.
Datatype: "CreditDebit3Code" on page 5291
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
66.1.42.1.2.9  SettlementInstructionReason <SttlmInstrRsn>
Presence: [0..1]
Definition: Type of transaction for which the cash account is specified.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5150 May 2026
```

