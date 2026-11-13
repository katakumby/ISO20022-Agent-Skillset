---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.6 ThirdPartyRights2"]
file_pages: [4596]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.6 ThirdPartyRights2

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4596 to 4596.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4596

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.24.6  ThirdPartyRights2
Definition: Information about third party rights.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 4596
   DateTime <DtTm> [0..1] DateTime 4596
   Holder <Hldr> [0..1] ± 4596
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4597
   Amount <Amt> [0..1] Amount C1, C13 4597
   Description <Desc> [0..1] Text 4597
66.1.24.6.1  Type <Tp>
Presence: [1..1]
Definition: Type of third party right.
Datatype: "Max35Text" on page 5403
66.1.24.6.2  DateTime <DtTm>
Presence: [0..1]
Definition: Timestamp for the third party right.
Datatype: "ISODateTime" on page 5388
66.1.24.6.3  Holder <Hldr>
Presence: [0..1]
Definition: Party that holds the third party right.
Holder <Hldr> contains one of the following elements (see "PartyIdentification125Choice" on
page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4596 May 2026
```

