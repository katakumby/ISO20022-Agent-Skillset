---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.8 LegInformation <LegInf>", "56.4.3.3.8.3 RepairedFee <RprdFee>", "56.4.3.3.8.3.1 Type <Tp>"]
file_pages: [4188, 4189]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.8.3.1 Type <Tp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4188 to 4189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4188

```text
RepairedFee <RprdFee> contains the following Fee12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  4188
{Or     Code <Cd> [1..1] CodeSet 4188
Or}     Proprietary <Prtry> [1..1] ± 4190
   RepairedStandardAmount <RprdStdAmt> [0..1] Amount C1, C8 4190
   RepairedStandardRate <RprdStdRate> [0..1] Rate 4190
   RepairedDiscountAmount <RprdDscntAmt> [0..1] Amount C1, C8 4190
   RepairedDiscountRate <RprdDscntRate> [0..1] Rate 4191
   RepairedRequestedAmount <RprdReqdAmt> [0..1] Amount C1, C8 4191
   RepairedRequestedRate <RprdReqdRate> [0..1] Rate 4191
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 4192
   NewCommercialAgreementReferenceIndicator
<NewComrclAgrmtRefInd>
[0..1] Indicator 4192
Constraints
• CommercialAgreementRule
If CommercialAgreementReference is present, then NewCommercialAgreementReferenceIndicator
must be present too.
On Condition
    /CommercialAgreementReference is present
Following Must be True
    /NewCommercialAgreementReferenceIndicator Must be present
• FeeElementRule
One of the elements (Type, RepairedStandardAmount, RepairedStandardRate,
RepairedDiscountAmount, RepairedDiscountRate, RepairedRequestedAmount,
RepairedRequestedRate, CommercialAgreementReference,
NewCommercialAgreementReferenceIndicator) must be present.
56.4.3.3.8.3.1  Type <Tp>
Presence: [0..1]
Definition: Type of fee (charge/commission).
Type <Tp> contains one of the following ChargeType10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4188
Or}   Proprietary <Prtry> [1..1] ± 4190
56.4.3.3.8.3.1.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4188 May 2026
```

## File page 4189

```text
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
INIT InitialCharge Charge paid at the time of the first
subscription.
PREM Premium In investment funds, pre-arranged
addition to the trade amount based on
the published net asset value.
CHAR ServiceProvisionFee Fee paid by the investor to a distributor/
intermediary or other service provider for
the provision of financial services.
SWIT Switch In investment funds, charge related to a
switch transaction.
UCIC UCITSCommission Charges paid by the investor to the fund
company for subscription and
redemption orders.
COMM Commission Amount paid out by the fund to a third
party.
SHIP ShippingCharge Charge for shipping, including the
insurance of securities.
POST PostageCharge Charge paid for the postage.
CDPL CommissionDePlacement Amount of cash due to an intermediary
for selling a product, or services, to a
third party.
ADDF AdditionalFee Additional fee not covered by another
fee type.
REGF RegulatoryFee Fee charged by a regulatory authority,
for example, securities and exchange
fees.
PENA Penalty Fee charged to the investor for early
redemption of the fund.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4189 May 2026
```

