---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.19 TransfereeAccount <TrfeeAcct>", "40.4.15.11.19.1 OwnerIdentification <OwnrId>"]
file_pages: [1640]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.19.1 OwnerIdentification <OwnrId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1640 to 1640.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1640

```text
TransfereeAccount <TrfeeAcct> contains the following Account37 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OwnerIdentification <OwnrId> [0..1] ± 1640
   AccountIdentification <AcctId> [0..1] Text 1640
   Designation <Dsgnt> [0..1] Text 1640
   AccountName <AcctNm> [0..1] Text 1640
   Servicer <Svcr> [0..1] ± 1641
   SubAccountDetails <SubAcctDtls> [0..1] ± 1641
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1641
40.4.15.11.19.1  OwnerIdentification <OwnrId>
Presence: [0..1]
Definition: Party that legally owns the account.
OwnerIdentification <OwnrId> contains the following elements (see "PartyIdentification132" on
page 5029 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
40.4.15.11.19.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
40.4.15.11.19.3  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 5403
40.4.15.11.19.4  AccountName <AcctNm>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1640 May 2026
```

