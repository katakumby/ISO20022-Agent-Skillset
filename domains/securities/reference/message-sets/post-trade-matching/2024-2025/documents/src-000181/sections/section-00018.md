---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "2.4 Message Building Blocks", "2.4.3 ConfirmationParties <ConfPties>", "2.4.3.10 ExecutingBroker <ExctgBrkr>"]
file_pages: [20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02"]
---

# 2.4.3.10 ExecutingBroker <ExctgBrkr>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 20 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 20

```text
ClearingFirm <ClrFirm> contains the following elements (see "ConfirmationPartyDetails13" on
page 414 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  415
{Or     BIC <BIC> [1..1] IdentifierSet C3 416
Or     ProprietaryIdentification <PrtryId> [1..1] ± 416
Or}     NameAndAddress <NmAndAdr> [1..1]  417
       Name <Nm> [1..1] Text 417
       Address <Adr> [0..1]  417
         AddressType <AdrTp> [0..1] CodeSet 418
         AddressLine <AdrLine> [0..5] Text 418
         StreetName <StrtNm> [0..1] Text 418
         BuildingNumber <BldgNb> [0..1] Text 418
         PostCode <PstCd> [0..1] Text 419
         TownName <TwnNm> [0..1] Text 419
         CountrySubDivision <CtrySubDvsn> [0..1] Text 419
         Country <Ctry> [1..1] CodeSet C4 419
   AlternateIdentification <AltrnId> [0..1] ± 419
   ProcessingIdentification <PrcgId> [0..1] Text 419
   AdditionalInformation <AddtlInf> [0..1] ± C1 420
   InvestorProtectionAssociationMembership
<InvstrPrtcnAssoctnMmbsh>
[0..1] Indicator 420
2.4.3.10  ExecutingBroker <ExctgBrkr>
Presence: [0..1]
Definition: Party responsible for executing an order (for example, an executing or give-up broker).
Usually a commission is charged to the client for executing an order.
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 20 February 2025
```

