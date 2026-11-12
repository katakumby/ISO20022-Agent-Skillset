---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.10 AdditionalReference13", "66.1.23.10.3 MessageName <MsgNm>"]
file_pages: [4547]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.10.3 MessageName <MsgNm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4547 to 4547.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4547

```text
ReferenceIssuer <RefIssr> contains one of the following elements (see "PartyIdentification125Choice"
on page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.23.10.3  MessageName <MsgNm>
Presence: [0..1]
Definition: Name of the message.
Datatype: "Max35Text" on page 5403
66.1.23.11  IdentificationType42Choice
Definition: Choice between a code and a data source scheme to specify the type of alternate
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4547
Or}   Proprietary <Prtry> [1..1] ± 4547
66.1.23.11.1  Code <Cd>
Presence: [1..1]
Definition: Type of identification is defined using a code.
Datatype: "TypeOfIdentification1Code" on page 5382
CodeName Name Definition
ARNU AlienRegistrationNumber Number assigned by a government
agency to identify foreign nationals.
CCPT PassportNumber Number assigned by a passport
authority.
CHTY TaxExemptIdentificationNumber Number assigned to a tax exempt entity.
CORP CorporateIdentification Number assigned to a corporate entity.
DRLC DriverLicenseNumber Number assigned to a driver's license.
FIIN ForeignInvestmentIdentityNumber Number assigned to a foreign investor
(other than the alien number).
TXID TaxIdentificationNumber Number assigned by a tax authority to
an entity.
66.1.23.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of identification is defined using a data source scheme.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4547 May 2026
```

