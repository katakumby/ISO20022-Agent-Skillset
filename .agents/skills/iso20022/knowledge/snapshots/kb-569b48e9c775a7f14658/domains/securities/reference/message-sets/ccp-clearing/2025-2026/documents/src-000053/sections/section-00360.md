---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.9 PartyIdentification253Choice"]
file_pages: [453]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.9 PartyIdentification253Choice

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 453 to 453.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 453

```text
12.1.14.9  PartyIdentification253Choice
Definition: Choice of identification of a party. The party can be identified by giving a BIC or a proprietary
code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 453
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 453
12.1.14.9.1  BIC <BIC>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Impacted by:   'C3 AnyBIC  '
Datatype: AnyBICDec2014Identifier on page 488
Constraints
• AnyBIC
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Error handling:
– Error severity: Fatal
– Error Code: D00008
– Error Text: Invalid BIC.
12.1.14.9.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see GenericIdentification36 on
page 399 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 399
   Issuer <Issr> [1..1] Text 400
   SchemeName <SchmeNm> [0..1] Text 400
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 453
```

