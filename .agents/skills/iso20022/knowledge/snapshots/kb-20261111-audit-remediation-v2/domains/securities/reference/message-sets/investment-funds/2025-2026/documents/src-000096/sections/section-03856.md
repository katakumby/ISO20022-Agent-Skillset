---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.41 Service Level Agreement", "66.1.41.2 DocumentToSend4", "66.1.41.2.2 Recipient <Rcpt>"]
file_pages: [5145]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.41.2.2 Recipient <Rcpt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5145 to 5145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5145

```text
66.1.41.2.2  Recipient <Rcpt>
Presence: [1..1]
Definition: Party that should receive the document.
Recipient <Rcpt> contains one of the following elements (see "PartyIdentification125Choice" on
page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.41.2.3  MethodOfTransmission <MtdOfTrnsmssn>
Presence: [1..1]
Definition: Communication method to be used.
MethodOfTransmission <MtdOfTrnsmssn> contains one of the following
CommunicationMethod3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5145
Or}   Proprietary <Prtry> [1..1] ± 5145
66.1.41.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Method of transmission expressed as a code.
Datatype: "CommunicationMethod1Code" on page 5285
CodeName Name Definition
SWMT SWIFTMT Transmission by Swift (FIN).
SWMX SWIFTMX Transmission by SWIFTNET.
FAXI Fax Transmission by fax.
EMAL Email Transmission by e-mail.
PROP Proprietary Transmission by proprietary method.
66.1.41.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Method of transmission expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5145 May 2026
```

