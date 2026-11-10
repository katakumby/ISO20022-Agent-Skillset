---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.20 Transferor <Trfr>"]
file_pages: [1259]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.20 Transferor <Trfr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1259 to 1259.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1259

```text
36.4.15.11.20  Transferor <Trfr>
Presence: [0..1]
Definition: Party and account from which the transferor delivers the financial instrument to the
transferee.
Transferor <Trfr> contains the following Account37 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OwnerIdentification <OwnrId> [0..1] ± 1259
   AccountIdentification <AcctId> [0..1] Text 1259
   Designation <Dsgnt> [0..1] Text 1259
   AccountName <AcctNm> [0..1] Text 1260
   Servicer <Svcr> [0..1] ± 1260
   SubAccountDetails <SubAcctDtls> [0..1] ± 1260
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1260
36.4.15.11.20.1  OwnerIdentification <OwnrId>
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
36.4.15.11.20.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
36.4.15.11.20.3  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1259 May 2026
```

