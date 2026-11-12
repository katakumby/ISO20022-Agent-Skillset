---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.23 InvestorProfile2"]
file_pages: [4847]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.23 InvestorProfile2

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4847 to 4847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4847

```text
Datatype: "Max70Text" on page 5404
66.1.28.23  InvestorProfile2
Definition: Information about actions that may be taken on an account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  4847
{Or     Code <Cd> [1..1] CodeSet 4848
Or}     Proprietary <Prtry> [1..1] ± 4848
   Status <Sts> [0..1]  4849
{Or     Code <Cd> [1..1] CodeSet 4849
Or}     Proprietary <Prtry> [1..1] ± 4849
   Treasury <Trsr> [0..1]  4850
     Date <Dt> [1..1] Date 4850
     TraderType <TradrTp> [1..1]  4850
{Or       Code <Cd> [1..1] CodeSet 4850
Or}       Proprietary <Prtry> [1..1] ± 4851
     Rate <Rate> [1..1] Rate 4851
   HighFrequencyTrading <HghFrqcyTradg> [0..1]  4851
     Date <Dt> [0..1] Date 4851
     SettlementFrequency <SttlmFrqcy> [0..1]  4852
{Or       Code <Cd> [1..1] CodeSet 4852
Or}       Proprietary <Prtry> [1..1] ± 4852
     ConsolidationType <CnsldtnTp> [0..1]  4852
{Or       Code <Cd> [1..1] CodeSet 4853
Or}       Proprietary <Prtry> [1..1] ± 4853
   MarketMaker <MktMakr> [0..1]  4853
     ContractPeriod <CtrctPrd> [0..1] ± 4853
     Compliance <Cmplc> [0..1] Indicator 4854
     MaximumSpread <MaxSprd> [0..1] Rate 4854
     Discount <Dscnt> [0..1] Rate 4854
66.1.28.23.1  Type <Tp>
Presence: [0..1]
Definition: Type of profile.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4847 May 2026
```

