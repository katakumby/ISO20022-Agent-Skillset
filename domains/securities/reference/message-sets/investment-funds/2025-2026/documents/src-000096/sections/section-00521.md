---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.11 TransferReason <TrfRsn>"]
file_pages: [715, 716]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.11 TransferReason <TrfRsn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 715 to 716.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 715

```text
Definition: Date on which the investor signed the transfer order form.
Datatype: "ISODate" on page 5388
30.4.7.11  TransferReason <TrfRsn>
Presence: [0..1]
Definition: Reason for the transfer.
TransferReason <TrfRsn> contains one of the following elements (see "TransferReason1Choice" on
page 5265 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5266
Or}   Proprietary <Prtry> [1..1] ± 5266
30.4.7.12  HoldingsPlanType <HldgsPlanTp>
Presence: [0..3]
Definition: Specifies information about investment plans included in the holding.
Datatype: "HoldingsPlanType1Code" on page 5309
CodeName Name Definition
INVP InvestmentPlan Holding to be transferred belongs to an
investment plan.
SWIP SwitchPlan Holding to be transferred belongs to a
switch plan.
PLAR WithdrawalPlan Holding to be transferred belongs to a
withdrawal plan.
30.4.7.13  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Information related to the financial instrument transferred.
Impacted by: C20 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 715 May 2026
```

## File page 716

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument116
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  717
{Or     ISIN <ISIN> [1..1] IdentifierSet 717
Or     SEDOL <SEDOL> [1..1] IdentifierSet 717
Or     CUSIP <CUSIP> [1..1] IdentifierSet 718
Or     RIC <RIC> [1..1] IdentifierSet 718
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 718
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 718
Or     CTA <CTA> [1..1] IdentifierSet 718
Or     QUICK <QUICK> [1..1] IdentifierSet 718
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 718
Or     Dutch <Dtch> [1..1] IdentifierSet 719
Or     Valoren <Vlrn> [1..1] IdentifierSet 719
Or     Sicovam <SCVM> [1..1] IdentifierSet 719
Or     Belgian <Belgn> [1..1] IdentifierSet 719
Or     Common <Cmon> [1..1] IdentifierSet 719
Or     DTI <DTI> [1..1] IdentifierSet 719
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  719
       Identification <Id> [1..1] Text 720
       IdentificationSource <IdSrc> [1..1] ± 720
   Name <Nm> [0..1] Text 720
   ShortName <ShrtNm> [0..1] Text 720
   SupplementaryIdentification <SplmtryId> [0..1] Text 720
   ClassType <ClssTp> [0..1] Text 720
   SecuritiesForm <SctiesForm> [0..1] CodeSet 721
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 721
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 721
Constraints
• IdentificationGuideline
It is recommended that ISIN is used in Identification.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 716 May 2026
```

