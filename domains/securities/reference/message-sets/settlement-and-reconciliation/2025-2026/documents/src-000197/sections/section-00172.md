---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.8 SubAccountDetails <SubAcctDtls>", "8.4.8.5 FinancialInstrumentDetails <FinInstrmDtls>", "8.4.8.5.2 InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts>"]
file_pages: [250]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.8.5.2 InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 250 to 250.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 250

```text
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
8.4.8.5.2  InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising an investment funds financial instrument.
InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts> contains the
following elements (see "FinancialInstrument72" on page 1473 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SupplementaryIdentification <SplmtryId> [0..1] Text 1473
   SecuritiesForm <SctiesForm> [0..1] CodeSet 1473
   ClassType <ClssTp> [0..1] Text 1473
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 1473
   ClassificationType <ClssfctnTp> [0..1] ± 1474
8.4.8.5.3  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Information regarding the price of the instrument.
Impacted by: C47 "ValueRule"
PriceDetails <PricDtls> contains the following elements (see "PriceInformation30" on page 1706 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1707
   ValueType <ValTp> [1..1] ± 1707
   Value <Val> [1..1] ± 1707
   SourceOfPrice <SrcOfPric> [0..1] ± C35 1707
   QuotationDate <QtnDt> [0..1] ± 1708
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 250 March 2026
```

