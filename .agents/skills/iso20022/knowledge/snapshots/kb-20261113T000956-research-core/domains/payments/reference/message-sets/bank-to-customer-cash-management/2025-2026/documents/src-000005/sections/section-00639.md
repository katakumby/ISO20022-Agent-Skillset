---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.18 Person Identification"]
file_pages: [872]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.18 Person Identification

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 872 to 872.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 872

```text
6.1.18 Person Identification
6.1.18.1  Contact13
Definition: Specifies the details of the contact person.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 872
   Name <Nm> [0..1] Text 872
   PhoneNumber <PhneNb> [0..1] Text 873
   MobileNumber <MobNb> [0..1] Text 873
   FaxNumber <FaxNb> [0..1] Text 873
   URLAddress <URLAdr> [0..1] Text 873
   EmailAddress <EmailAdr> [0..1] Text 873
   EmailPurpose <EmailPurp> [0..1] Text 873
   JobTitle <JobTitl> [0..1] Text 873
   Responsibility <Rspnsblty> [0..1] Text 873
   Department <Dept> [0..1] Text 874
   Other <Othr> [0..*]  874
     ChannelType <ChanlTp> [1..1] Text 874
     Identification <Id> [0..1] Text 874
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 874
6.1.18.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 901
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
6.1.18.1.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
872 March 2026
```

