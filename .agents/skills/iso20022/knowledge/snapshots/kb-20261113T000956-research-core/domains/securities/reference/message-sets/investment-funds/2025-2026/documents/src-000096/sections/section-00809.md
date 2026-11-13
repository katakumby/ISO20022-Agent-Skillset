---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.25 SettlementPartiesDetails <SttlmPtiesDtls>", "35.4.14.10.25.5 ReceivingSideDetails <RcvgSdDtls>", "35.4.14.10.25.5.2 Party1 <Pty1>"]
file_pages: [1097]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.25.5.2 Party1 <Pty1>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1097 to 1097.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1097

```text
Depository <Dpstry> contains the following elements (see "PartyIdentification315" on page 4906 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  4906
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4907
Or     NameAndAddress <NmAndAdr> [1..1] ± 4907
Or     Country <Ctry> [1..1] CodeSet C12 4907
Or}     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4908
   LEI <LEI> [0..1] IdentifierSet 4908
   AlternateIdentification <AltrnId> [0..1] ± 4908
   ProcessingDate <PrcgDt> [0..1] ± 4908
   ProcessingIdentification <PrcgId> [0..1] Text 4908
   AdditionalInformation <AddtlInf> [0..1] ± C3 4909
35.4.14.10.25.5.2  Party1 <Pty1>
Presence: [0..1]
Definition: Party that, in a settlement chain, interacts with the depository.
Party1 <Pty1> contains the following elements (see "PartyIdentificationAndAccount194" on page 5009
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5010
   LEI <LEI> [0..1] IdentifierSet 5010
   AlternateIdentification <AltrnId> [0..1] ± 5010
   SafekeepingAccount <SfkpgAcct> [0..1] ± 5010
   ProcessingDate <PrcgDt> [0..1] ± 5011
   ProcessingIdentification <PrcgId> [0..1] Text 5011
   AdditionalInformation <AddtlInf> [0..1] ± C4 5011
35.4.14.10.25.5.3  Party2 <Pty2>
Presence: [0..1]
Definition: Party that, in a settlement chain, interacts with the party 1.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1097 May 2026
```

