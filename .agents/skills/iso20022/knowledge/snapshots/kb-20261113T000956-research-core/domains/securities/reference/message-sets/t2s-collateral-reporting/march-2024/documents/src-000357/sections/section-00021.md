---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 BusinessReport <BizRpt>", "3.4.2.1.1 CashAccount <CshAcct>"]
file_pages: [24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.4.2.1.1 CashAccount <CshAcct>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 24 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             QuantityAndAvailability <QtyAndAvlbty> [1..1]  36
               Quantity <Qty> [1..1] ± 36
               AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 36
         ValuationPrice <ValtnPric> [1..1]  36
           AmountPriceType <AmtPricTp> [1..1] ± 37
           PriceValue <PricVal> [1..1] ± 37
           FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 37
           PriceFixingDate <PricFxgDt> [1..1] Date 38
         CollateralValue <CollVal> [1..1] Amount C1, C6 38
3.4.2.1.1  CashAccount <CshAcct>
Presence: [1..1]
Definition: Unique identification, as assigned by the account servicer, to unambiguously identify the
account on which information is requested.
Impacted by: C11 "IdentificationOrProxyPresenceRule", C10 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 40 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 41
   Type <Tp> [0..1] ± 41
   Currency <Ccy> [0..1] CodeSet C2 41
   Name <Nm> [0..1] Text 42
   Proxy <Prxy> [0..1] ± 42
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
24 March 2024
```

