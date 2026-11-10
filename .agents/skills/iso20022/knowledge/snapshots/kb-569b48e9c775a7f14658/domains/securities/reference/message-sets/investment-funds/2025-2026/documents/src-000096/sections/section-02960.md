---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.10 OrderData <OrdrData>", "56.4.3.2.10.1 InvestmentAccountDetails <InvstmtAcctDtls>"]
file_pages: [4154]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.10.1 InvestmentAccountDetails <InvstmtAcctDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4154 to 4154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4154

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SupplementaryIdentification <SplmtryId> [0..1] Text 4162
     ClassType <ClssTp> [0..1] Text 4162
     SecuritiesForm <SctiesForm> [0..1] CodeSet 4163
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4163
     ProductGroup <PdctGrp> [0..1] Text 4163
     SeriesIdentification <SrsId> [0..1]  C19 4163
       SeriesDate <SrsDt> [0..1] ± 4164
       SeriesName <SrsNm> [0..1] Text 4164
   UnitsNumber <UnitsNb> [0..1] Quantity 4164
   DigitalTokenUnit <DgtlTknUnit> [0..1] Quantity 4164
   NetAmount <NetAmt> [0..1] Amount C2, C9 4164
   GrossAmount <GrssAmt> [0..1] Amount C2, C9 4165
   HoldingsRedemptionRate <HldgsRedRate> [0..1] Rate 4165
   SettlementAmount <SttlmAmt> [0..1] Amount C1, C8 4165
   UnitCurrency <UnitCcy> [0..1] CodeSet C1 4166
   QuotedCurrency <QtdCcy> [0..1] CodeSet C1 4166
Constraints
• OrderDataElementRule
One of the elements (InvestmentAccountDetails, FinancialInstrumentDetails, UnitsNumber,
NetAmount, GrossAmount, HoldingsRedemptionRate, SettlementAmount, UnitCurrency,
QuotedCurrency) must be present.
56.4.3.2.10.1  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Account information of the individual order instruction for which the status is given.
Impacted by: C16 "OrderOriginatorEligibility2Rule"
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4154 May 2026
```

