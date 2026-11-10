---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.1 CashAccount <CshAcct>"]
file_pages: [598]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.4.2.1.1 CashAccount <CshAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 598 to 598.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 598

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             QuantityAndAvailability <QtyAndAvlbty> [1..1]  610
               Quantity <Qty> [1..1] ± 610
               AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 610
         ValuationPrice <ValtnPric> [1..1]  610
           AmountPriceType <AmtPricTp> [1..1] ± 611
           PriceValue <PricVal> [1..1] ± 611
           FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 611
           PriceFixingDate <PricFxgDt> [1..1] Date 612
         CollateralValue <CollVal> [1..1] Amount C1, C6 612
25.4.2.1.1  CashAccount <CshAcct>
Presence: [1..1]
Definition: Unique identification, as assigned by the account servicer, to unambiguously identify the
account on which information is requested.
Impacted by: C11 "IdentificationOrProxyPresenceRule", C10 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 2832 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 2832
   Type <Tp> [0..1] ± 2832
   Currency <Ccy> [0..1] CodeSet C1 2833
   Name <Nm> [0..1] Text 2833
   Proxy <Prxy> [0..1] ± 2833
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 598 August 2026
```

