---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.20 PeriodDetails <PrdDtls>"]
file_pages: [153]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.20 PeriodDetails <PrdDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 153 to 153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 153

```text
DocumentationDeadline <DcmnttnDdln> contains one of the following elements (see
"DateFormat46Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 846
Or}   DateCode <DtCd> [1..1]  846
{Or     Code <Cd> [1..1] CodeSet 846
Or}     Proprietary <Prtry> [1..1] ± 846
3.4.11.20  PeriodDetails <PrdDtls>
Presence: [0..1]
Definition: Provides information about the periods related to a corporate action option.
PeriodDetails <PrdDtls> contains the following CorporateActionPeriod18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PriceCalculationPeriod <PricClctnPrd> [0..1] ± 153
   ParallelTradingPeriod <ParllTradgPrd> [0..1] ± 153
   ActionPeriod <ActnPrd> [0..1] ± 154
   RevocabilityPeriod <RvcbltyPrd> [0..1] ± 154
   PrivilegeSuspensionPeriod <PrvlgSspnsnPrd> [0..1] ± 154
   AccountServicerRevocabilityPeriod
<AcctSvcrRvcbltyPrd>
[0..1] ± 154
   DepositorySuspensionPeriodForWithdrawal
<DpstrySspnsnPrdForWdrwl>
[0..1] ± 155
3.4.11.20.1  PriceCalculationPeriod <PricClctnPrd>
Presence: [0..1]
Definition: Period during which the price of a security is determined.
PriceCalculationPeriod <PricClctnPrd> contains one of the following elements (see
"Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
3.4.11.20.2  ParallelTradingPeriod <ParllTradgPrd>
Presence: [0..1]
Definition: Period during which both old and new equity may be traded simultaneously, for example,
consolidation of equity or splitting of equity.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 153 February 2026
```

