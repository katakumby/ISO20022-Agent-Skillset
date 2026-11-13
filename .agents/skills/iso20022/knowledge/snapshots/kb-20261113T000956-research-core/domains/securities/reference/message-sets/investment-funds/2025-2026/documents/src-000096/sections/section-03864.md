---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction", "66.1.42.1 CashSettlement4", "66.1.42.1.2 CashAccountDetails <CshAcctDtls>", "66.1.42.1.2.11 CashAccountDesignation <CshAcctDsgnt>"]
file_pages: [5153]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42.1.2.11 CashAccountDesignation <CshAcctDsgnt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5153 to 5153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5153

```text
66.1.42.1.2.11  CashAccountDesignation <CshAcctDsgnt>
Presence: [0..1]
Definition: Specifies whether the account is the primary or secondary account if there are two accounts
for the same purpose.
CashAccountDesignation <CshAcctDsgnt> contains one of the following
AccountDesignation1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5153
Or}   Proprietary <Prtry> [1..1] ± 5153
66.1.42.1.2.11.1  Code <Cd>
Presence: [1..1]
Definition: Account designation expressed as a code.
Datatype: "Rank1Code" on page 5346
CodeName Name Definition
PRIM Primary Element is the primary one.
SECO Secondary Element is the primary one.
66.1.42.1.2.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Account designation expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.42.1.2.12  DividendPercentage <DvddPctg>
Presence: [0..1]
Definition: Percentage of the dividend payment not to be reinvested, that is, to be paid in cash.
Datatype: "PercentageBoundedRate" on page 5401
66.1.42.1.3  OtherCashSettlementDetails <OthrCshSttlmDtls>
Presence: [0..*]
Definition: Method of payment other than a cash account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5153 May 2026
```

