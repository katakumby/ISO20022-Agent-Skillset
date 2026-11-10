---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.16 RelatedRemittanceInformation <RltdRmtInf>", "5.4.2.18.16.2 RemittanceLocationDetails <RmtLctnDtls>", "5.4.2.18.16.2.2 ElectronicAddress <ElctrncAdr>"]
file_pages: [483]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.16.2.2 ElectronicAddress <ElctrncAdr>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 483 to 483.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 483

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
5.4.2.18.16.2.2  ElectronicAddress <ElctrncAdr>
Presence: [0..1]
Definition: Electronic address to which an agent is to send the remittance information.
Datatype: "Max2048Text" on page 608
5.4.2.18.16.2.3  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Postal address to which an agent is to send the remittance information.
PostalAddress <PstlAdr> contains the following NameAndAddress18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 483
   Address <Adr> [1..1] ± 483
5.4.2.18.16.2.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and is usually used to identify that party.
Datatype: "Max140Text" on page 608
5.4.2.18.16.2.3.2  Address <Adr>
Presence: [1..1]
Definition: Postal address of a party.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 483 March 2026
```

