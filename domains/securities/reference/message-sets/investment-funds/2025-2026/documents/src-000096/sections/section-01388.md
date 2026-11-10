---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.19 PartiallyExecutedIndicator <PrtlyExctdInd>"]
file_pages: [1954]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.19 PartiallyExecutedIndicator <PrtlyExctdInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1954 to 1954.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1954

```text
InformativePriceDetails <InftvPricDtls> contains the following elements (see "UnitPrice22" on
page 5109 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 5109
   Value <Val> [1..1] ± 5110
   PriceMethod <PricMtd> [0..1] CodeSet 5110
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 5110
   TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C1 5110
   TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1]  5111
{Or     Code <Cd> [1..1] CodeSet 5111
Or}     Proprietary <Prtry> [1..1] ± 5111
   PriceDifferenceReason <PricDiffRsn> [0..1] Text 5112
43.4.5.9.19  PartiallyExecutedIndicator <PrtlyExctdInd>
Presence: [1..1]
Definition: Indicates whether the order has been partially executed, that is, the confirmed quantity does
not match the ordered quantity for a given financial instrument.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
43.4.5.9.20  BestExecution <BestExctn>
Presence: [0..1]
Definition: Specifies that the execution was subject to best execution rules as defined by MiFID.
Datatype: "BestExecution1Code" on page 5278
CodeName Name Definition
BTEX Best Best execution rules were followed.
43.4.5.9.21  CumDividendIndicator <CumDvddInd>
Presence: [1..1]
Definition: Indicates whether the dividend is included, that is, cum-dividend, in the executed price. When
the dividend is not included, the price will be ex-dividend.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1954 May 2026
```

