---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.4 Message Building Blocks", "32.4.2.8 InvestmentAccountDetails <InvstmtAcctDtls>", "32.4.2.8.4 AccountName <AcctNm>"]
file_pages: [802]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.4.2.8.4 AccountName <AcctNm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 802 to 802.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 802

```text
32.4.2.8.4  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
32.4.2.8.5  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   Issuer <Issr> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4553
32.4.2.8.6  Servicer <Svcr>
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
32.4.2.8.7  SubAccountDetails <SubAcctDtls>
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
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 802 May 2026
```

