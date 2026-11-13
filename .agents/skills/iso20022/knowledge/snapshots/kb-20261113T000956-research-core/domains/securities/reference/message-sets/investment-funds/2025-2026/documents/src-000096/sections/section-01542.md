---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.15 TransactionOverhead <TxOvrhd>", "44.4.4.9.15.2 IndividualFee <IndvFee>", "44.4.4.9.15.2.1 Type <Tp>"]
file_pages: [2166]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.15.2.1 Type <Tp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2166 to 2166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2166

```text
Constraints
• FeeElementRule
One of the elements (Basis, StandardAmount, StandardRate, DiscountDetails, RequestedAmount,
RequestedRate, NonStandardSLAReference, RecipientIdentification) must be present.
• StandardFeeAmountCalculation
If StandardAmount, RequestedAmount and DiscountDetails/Amount are all present, then
StandardAmount minus DiscountDetails/Amount must equal RequestedAmount.
• StandardFeeRateCalculation
If StandardRate, RequestedRate and DiscountDetails/Rate are all present, then StandardRate minus
DiscountDetails/Rate must equal RequestedRate.
44.4.4.9.15.2.1  Type <Tp>
Presence: [1..1]
Definition: Type of fee (charge/commission).
Type <Tp> contains one of the following ChargeType10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2166
Or}   Proprietary <Prtry> [1..1] ± 2167
44.4.4.9.15.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Fee (charge/commission) expressed as a code.
Datatype: "InvestmentFundFee3Code" on page 0
CodeName Name Definition
BEND BackEndLoad Fee paid by the investor to the fund or
fund management company when
redeeming.
BRKF BrokerageFee Fee paid to a broker for services
provided.
CDSC ContingentDeferredSalesCharge Deferred sales charge.
CBCH CorrespondentBankCharge In investment funds, the charge of the
correspondent bank for transferring
money.
DLEV DilutionLevy In investment funds, a charge payable
by the investor covering bid-offer
spreads and dealing charges for the
underlying investments. The dilution levy
is paid to the fund for the benefit of other
unit holders.
FEND FrontEndLoad Fee paid by the investor to the fund or
fund management company when
subscribing.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2166 May 2026
```

