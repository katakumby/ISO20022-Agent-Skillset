---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.6 Miscellaneous", "4.1.6.4 OriginalBusinessInstruction1", "4.1.6.4.3 CreationDateTime <CreDtTm>"]
file_pages: [35]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.6.4.3 CreationDateTime <CreDtTm>

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 35 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
Datatype: "Max35Text" on page 46
4.1.6.4.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 43
4.1.7 Party Identification
4.1.7.1  PartyIdentification120Choice
Definition: Choice between different formats for the identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 35
Or   ProprietaryIdentification <PrtryId> [1..1] ± 35
Or}   NameAndAddress <NmAndAdr> [1..1] ± 36
4.1.7.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 44
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
4.1.7.1.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
Message Items Types
Target2-Securities - Limit Utilisation Journal 35 February 2025
```

