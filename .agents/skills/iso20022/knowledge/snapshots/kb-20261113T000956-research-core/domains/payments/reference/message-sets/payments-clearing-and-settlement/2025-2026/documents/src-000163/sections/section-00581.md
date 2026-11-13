---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.46 RelatedRemittanceInformation <RltdRmtInf>", "6.4.2.46.2 RemittanceLocationDetails <RmtLctnDtls>", "6.4.2.46.2.2 ElectronicAddress <ElctrncAdr>"]
file_pages: [786]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.46.2.2 ElectronicAddress <ElctrncAdr>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 786 to 786.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 786

```text
CodeName Name Definition
EDIC ElectronicDataInterchange Remittance advice information must be
sent through Electronic Data Interchange
(EDI).
URID UniformResourceIdentifier Remittance advice information needs to
be sent to a Uniform Resource Identifier
(URI). URI is a compact string of
characters that uniquely identify an
abstract or physical resource. URI's are
the super-set of identifiers, such as
URLs, email addresses, ftp sites, etc,
and as such, provide the syntax for all of
the identification schemes.
EMAL EMail Remittance advice information must be
sent through e-mail.
POST Post Remittance advice information must be
sent through postal services.
SMSM SMS Remittance advice information must be
sent through by phone as a short
message service (SMS).
6.4.2.46.2.2  ElectronicAddress <ElctrncAdr>
Presence: [0..1]
Definition: Electronic address to which an agent is to send the remittance information.
Datatype: "Max2048Text" on page 1245
6.4.2.46.2.3  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Postal address to which an agent is to send the remittance information.
PostalAddress <PstlAdr> contains the following NameAndAddress18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 786
   Address <Adr> [1..1] ± 786
6.4.2.46.2.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and is usually used to identify that party.
Datatype: "Max140Text" on page 1244
6.4.2.46.2.3.2  Address <Adr>
Presence: [1..1]
Definition: Postal address of a party.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
786 March 2026
```

