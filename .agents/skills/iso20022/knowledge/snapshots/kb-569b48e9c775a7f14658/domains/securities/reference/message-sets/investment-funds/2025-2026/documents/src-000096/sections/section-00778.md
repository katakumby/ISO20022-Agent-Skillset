---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.16 TransfereeAccount <TrfeeAcct>", "35.4.14.10.16.3 Designation <Dsgnt>"]
file_pages: [1062]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.16.3 Designation <Dsgnt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1062 to 1062.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1062

```text
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
35.4.14.10.16.3  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 5403
35.4.14.10.16.4  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
35.4.14.10.16.5  Servicer <Svcr>
Presence: [0..1]
Definition: Institution that maintains the records where the account is held.
Servicer <Svcr> contains the following elements (see "PartyIdentification132" on page 5029 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
35.4.14.10.16.6  SubAccountDetails <SubAcctDtls>
Presence: [0..1]
Definition: Sub-account of the master or omnibus account.
SubAccountDetails <SubAcctDtls> contains the following elements (see "SubAccount5" on
page 4329 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4329
   Name <Nm> [0..1] Text 4329
   Characteristic <Chrtc> [0..1] Text 4329
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1062 May 2026
```

