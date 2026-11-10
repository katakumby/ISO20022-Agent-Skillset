---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.16 TransfereeAccount <TrfeeAcct>"]
file_pages: [1061]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.16 TransfereeAccount <TrfeeAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1061 to 1061.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1061

```text
TotalBookValue <TtlBookVal> contains the following elements (see "DateAndAmount2" on page 4343
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [0..1] Date 4343
   Amount <Amt> [1..1] Amount C2, C10 4343
35.4.14.10.16  TransfereeAccount <TrfeeAcct>
Presence: [0..1]
Definition: Account held in the name of the party that is not the name of the beneficial owner of the
shares.
(Party and account into which the transferee receives the financial instrument from the transferor.)
TransfereeAccount <TrfeeAcct> contains the following Account37 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OwnerIdentification <OwnrId> [0..1] ± 1061
   AccountIdentification <AcctId> [0..1] Text 1061
   Designation <Dsgnt> [0..1] Text 1062
   AccountName <AcctNm> [0..1] Text 1062
   Servicer <Svcr> [0..1] ± 1062
   SubAccountDetails <SubAcctDtls> [0..1] ± 1062
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1063
35.4.14.10.16.1  OwnerIdentification <OwnrId>
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
35.4.14.10.16.2  AccountIdentification <AcctId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1061 May 2026
```

