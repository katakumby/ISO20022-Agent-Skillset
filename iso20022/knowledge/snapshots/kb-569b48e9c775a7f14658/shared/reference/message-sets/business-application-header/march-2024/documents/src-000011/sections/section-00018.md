---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04", "2.4 Message Building Blocks", "2.4.14 Related <Rltd>", "2.4.14.3 To <To>"]
file_pages: [20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2.4.14.3 To <To>

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 20 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 20

```text
FinancialInstitutionIdentification <FIId> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 26 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  27
     BICFI <BICFI> [0..1] IdentifierSet C2 27
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 28
     LEI <LEI> [0..1] IdentifierSet 28
     Name <Nm> [0..1] Text 28
     PostalAddress <PstlAdr> [0..1] ± 28
     Other <Othr> [0..1] ± 29
   BranchIdentification <BrnchId> [0..1]  30
     Identification <Id> [0..1] Text 30
     LEI <LEI> [0..1] IdentifierSet 30
     Name <Nm> [0..1] Text 30
     PostalAddress <PstlAdr> [0..1] ± 30
2.4.14.3  To <To>
Presence: [1..1]
Definition: The MessagingEndpoint designated by the sending MessagingEndpoint to be the recipient
who will ultimately process this Business Message.
Note the receiving MessagingEndpoint might be different from the receiving address potentially
contained in the transport header (as defined in the transport layer).
To <To> contains one of the following Party51Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 20
Or}   FinancialInstitutionIdentification <FIId> [1..1] ± 21
2.4.14.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Identification of a person or an organisation.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 20 March 2024
```

