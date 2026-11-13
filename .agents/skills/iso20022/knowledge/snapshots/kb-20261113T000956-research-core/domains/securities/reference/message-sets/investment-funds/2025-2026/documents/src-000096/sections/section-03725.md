---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.24 PartyIdentificationAndAccount194", "66.1.30.24.5 ProcessingDate <PrcgDt>"]
file_pages: [5011]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.24.5 ProcessingDate <PrcgDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5011 to 5011.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5011

```text
Definition: Identification of the account owned by the party.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 4323 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4323
   Type <Tp> [0..1] ± 4323
   Name <Nm> [0..1] Text 4323
66.1.30.24.5  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date/time at which the instruction was processed by the specified party.
ProcessingDate <PrcgDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
66.1.30.24.6  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 5403
66.1.30.24.7  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the party.
Impacted by: C4 "AdditonalDetailsGuideline"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation6" on
page 5028 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 5028
   PartyContactDetails <PtyCtctDtls> [0..1] Text 5028
   RegistrationDetails <RegnDtls> [0..1] Text 5028
   RegistrationAddress <RegnAdr> [0..1] ± 5028
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5011 May 2026
```

