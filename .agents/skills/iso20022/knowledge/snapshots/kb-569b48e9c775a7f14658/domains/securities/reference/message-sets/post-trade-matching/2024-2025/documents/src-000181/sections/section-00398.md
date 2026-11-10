---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.21 PartyIdentification245Choice"]
file_pages: [464]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.21 PartyIdentification245Choice

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 464 to 464.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 464

```text
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in a
structured field.
7.1.20.21  PartyIdentification245Choice
Definition: Choice of identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 464
Or   ProprietaryIdentification <PrtryId> [1..1] ± 464
Or}   NameAndAddress <NmAndAdr> [1..1] ± 464
7.1.20.21.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 662
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.1.20.21.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 280 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 280
   SchemeName <SchmeNm> [0..1] Text 280
   Issuer <Issr> [0..1] Text 281
7.1.20.21.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 464 February 2025
```

