---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.7 Financial Instrument Identification", "12.1.7.1 SecurityIdentification48", "12.1.7.1.2 OtherIdentification <OthrId>", "12.1.7.1.2.2 Suffix <Sfx>"]
file_pages: [393]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.7.1.2.2 Suffix <Sfx>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 393 to 393.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 393

```text
Datatype: Max35Text on page 493
12.1.7.1.2.2  Suffix <Sfx>
Presence: [0..1]
Definition: Identifies the suffix of the security identification.
Datatype: Max16Text on page 492
12.1.7.1.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see IdentificationSource3Choice on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 400
Or}   Proprietary <Prtry> [1..1] Text 400
12.1.7.1.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: Max140Text on page 492
12.1.7.2  SecurityIdentification14
Definition: Identification of a security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 394
   OtherIdentification <OthrId> [0..*]  395
     Identification <Id> [1..1] Text 395
     Suffix <Sfx> [0..1] Text 395
     Type <Tp> [1..1] ± 395
   Description <Desc> [0..1] Text 395
Constraints
• DescriptionPresenceRule
(Rule)
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 393
```

