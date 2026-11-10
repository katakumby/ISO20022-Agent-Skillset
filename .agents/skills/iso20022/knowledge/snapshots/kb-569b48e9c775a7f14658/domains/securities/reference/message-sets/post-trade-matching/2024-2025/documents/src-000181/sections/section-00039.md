---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.26 NumberOfDaysAccrued <NbOfDaysAcrd>"]
file_pages: [58]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.26 NumberOfDaysAccrued <NbOfDaysAcrd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 58 to 58.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 58

```text
Commission <Comssn> contains the following elements (see "Commission24" on page 257 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 257
   Commission <Comssn> [1..1] ± 257
   RecipientIdentification <RcptId> [0..1] ± 258
   CalculationDate <ClctnDt> [0..1] Date 258
   TotalCommission <TtlComssn> [0..1] ± 258
   TotalVATAmount <TtlVATAmt> [0..1] Amount C1, C9 259
   VATRate <VATRate> [0..1] Rate 259
3.4.4.26  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Number of days on which the interest rate accrues (daily accrual note).
Impacted by: C33 "NumberRule"
Datatype: "Max3Number" on page 666
Constraints
• NumberRule
If Number is negative, then Sign must be present.
3.4.4.27  GiveUpNumberOfDays <GvUpNbOfDays>
Presence: [0..1]
Definition: Specifies the number of days from trade date that the counterparty on the other side of the
trade should be "given up" or divulged.
Impacted by: C33 "NumberRule"
Datatype: "Max3Number" on page 666
Constraints
• NumberRule
If Number is negative, then Sign must be present.
3.4.4.28  InterestType <IntrstTp>
Presence: [0..1]
Definition: Indicates whether the trade is cum interest or ex interest.
Datatype: "InterestType2Code" on page 634
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 58 February 2025
```

