---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Person Identification", "7.1.20.1 Contact13", "7.1.20.1.1 NamePrefix <NmPrfx>"]
file_pages: [435]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.1.1 NamePrefix <NmPrfx>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 435 to 435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 435

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 435
   Name <Nm> [0..1] Text 435
   PhoneNumber <PhneNb> [0..1] Text 435
   MobileNumber <MobNb> [0..1] Text 436
   FaxNumber <FaxNb> [0..1] Text 436
   URLAddress <URLAdr> [0..1] Text 436
   EmailAddress <EmailAdr> [0..1] Text 436
   EmailPurpose <EmailPurp> [0..1] Text 436
   JobTitle <JobTitl> [0..1] Text 436
   Responsibility <Rspnsblty> [0..1] Text 436
   Department <Dept> [0..1] Text 436
   Other <Othr> [0..*]  437
     ChannelType <ChanlTp> [1..1] Text 437
     Identification <Id> [0..1] Text 437
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 437
7.1.20.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 515
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
7.1.20.1.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 556
7.1.20.1.3  PhoneNumber <PhneNb>
Presence: [0..1]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 435 March 2026
```

