---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.14 RelatedRemittanceInformation <RltdRmtInf>", "3.4.2.15.18.2.14.2 RemittanceLocationDetails <RmtLctnDtls>", "3.4.2.15.18.2.14.2.2 ElectronicAddress <ElctrncAdr>"]
file_pages: [425]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.14.2.2 ElectronicAddress <ElctrncAdr>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 425 to 425.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 425

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
3.4.2.15.18.2.14.2.2  ElectronicAddress <ElctrncAdr>
Presence: [0..1]
Definition: Electronic address to which an agent is to send the remittance information.
Datatype: "Max2048Text" on page 915
3.4.2.15.18.2.14.2.3  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Postal address to which an agent is to send the remittance information.
PostalAddress <PstlAdr> contains the following NameAndAddress18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 425
   Address <Adr> [1..1] ± 425
3.4.2.15.18.2.14.2.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and is usually used to identify that party.
Datatype: "Max140Text" on page 914
3.4.2.15.18.2.14.2.3.2  Address <Adr>
Presence: [1..1]
Definition: Postal address of a party.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
425 March 2026
```

