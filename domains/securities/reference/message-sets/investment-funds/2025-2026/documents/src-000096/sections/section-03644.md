---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.3 PartyIdentification1Choice", "66.1.29.3.1 BICOrBEI <BICOrBEI>"]
file_pages: [4894]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.3.1 BICOrBEI <BICOrBEI>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4894 to 4894.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4894

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4894
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4894
Or}   NameAndAddress <NmAndAdr> [1..1]  4894
     Name <Nm> [1..1] Text 4895
     Address <Adr> [0..1] ± 4895
66.1.29.3.1  BICOrBEI <BICOrBEI>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution.
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICIdentifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory, and
consists of eight (8) or eleven (11) contiguous characters.
66.1.29.3.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.29.3.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
NameAndAddress <NmAndAdr> contains the following NameAndAddress2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4895
   Address <Adr> [0..1] ± 4895
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4894 May 2026
```

