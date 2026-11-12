---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.8 RepairedFee <RprdFee>", "56.4.3.2.8.8 CommercialAgreementReference <ComrclAgrmtRef>"]
file_pages: [4152, 4153]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.8.8 CommercialAgreementReference <ComrclAgrmtRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4152 to 4153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4152

```text
Definition: Modified value of the requested fee (charge/commission) rate applied on the order (the
requested fee (charge/commission) rate in the original individual order that has been repaired so that
the order can be accepted).
Datatype: "PercentageRate" on page 5401
56.4.3.2.8.8  CommercialAgreementReference <ComrclAgrmtRef>
Presence: [0..1]
Definition: Reference to the agreement established between the fund and another party. This element,
amongst others, defines the conditions of the commissions.
Datatype: "Max35Text" on page 5403
56.4.3.2.8.9  NewCommercialAgreementReferenceIndicator <NewComrclAgrmtRefInd>
Presence: [0..1]
Definition: Indicates if the CommercialAgreementReference is a new reference or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
56.4.3.2.9  StatusInitiator <StsInitr>
Presence: [0..1]
Definition: Party that initiates the status of the order.
StatusInitiator <StsInitr> contains the following elements (see "PartyIdentification139" on page 5043
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
56.4.3.2.10  OrderData <OrdrData>
Presence: [0..1]
Definition: Order data.
Impacted by: C15 "OrderDataElementRule"
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4152 May 2026
```

## File page 4153

```text
OrderData <OrdrData> contains the following FundOrderData7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C16 4154
     AccountIdentification <AcctId> [1..1] Text 4155
     AccountName <AcctNm> [0..1] Text 4155
     AccountDesignation <AcctDsgnt> [0..1] Text 4155
     OwnerIdentification <OwnrId> [0..*] ± 4155
     AccountServicer <AcctSvcr> [0..1] ± 4156
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4156
     SubAccountDetails <SubAcctDtls> [0..1] ± 4156
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4157
   FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C13 4157
     Identification <Id> [1..1]  4159
{Or       ISIN <ISIN> [1..1] IdentifierSet 4159
Or       SEDOL <SEDOL> [1..1] IdentifierSet 4160
Or       CUSIP <CUSIP> [1..1] IdentifierSet 4160
Or       RIC <RIC> [1..1] IdentifierSet 4160
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 4160
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 4160
Or       CTA <CTA> [1..1] IdentifierSet 4160
Or       QUICK <QUICK> [1..1] IdentifierSet 4160
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 4161
Or       Dutch <Dtch> [1..1] IdentifierSet 4161
Or       Valoren <Vlrn> [1..1] IdentifierSet 4161
Or       Sicovam <SCVM> [1..1] IdentifierSet 4161
Or       Belgian <Belgn> [1..1] IdentifierSet 4161
Or       Common <Cmon> [1..1] IdentifierSet 4161
Or       DTI <DTI> [1..1] IdentifierSet 4161
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  4161
         Identification <Id> [1..1] Text 4162
         IdentificationSource <IdSrc> [1..1] ± 4162
     Name <Nm> [0..1] Text 4162
     ShortName <ShrtNm> [0..1] Text 4162
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4153 May 2026
```

