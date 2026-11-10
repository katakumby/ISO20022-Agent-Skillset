---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction", "66.1.42.2 CashSettlement3", "66.1.42.2.1 CashAccountDetails <CshAcctDtls>", "66.1.42.2.1.9 SettlementInstructionReason <SttlmInstrRsn>", "66.1.42.2.1.9.2 Proprietary <Prtry>"]
file_pages: [5160]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42.2.1.9.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5160 to 5160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5160

```text
CodeName Name Definition
CORP CorporateAction Settlement of corporate actions.
66.1.42.2.1.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement instruction reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.42.2.1.10  CashAccountPurpose <CshAcctPurp>
Presence: [0..1]
Definition: Purpose of the cash account.
CashAccountPurpose <CshAcctPurp> contains one of the following CashAccountType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5160
Or}   Proprietary <Prtry> [1..1] ± 5160
66.1.42.2.1.10.1  Code <Cd>
Presence: [1..1]
Definition: Type of cash account expressed as a code.
Datatype: "CashAccountType5Code" on page 5281
CodeName Name Definition
LEND Lending Account is for the coverage of lending.
COLL Collateral Account is for collateral.
SETT FinancialSettlement Account is for financial settlements.
MARR MarginReturn Account is for margin returns.
SEGT Segregated Account is an segregated account.
66.1.42.2.1.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of cash account expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5160 May 2026
```

