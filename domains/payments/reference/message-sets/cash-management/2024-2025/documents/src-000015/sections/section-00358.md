---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["14 camt.015.001.04 ModifyMemberV04", "14.4 Message Building Blocks", "14.4.3 NewMemberValueSet <NewMmbValSet>", "14.4.3.2 ContactReference <CtctRef>", "14.4.3.2.3 CommunicationAddress <ComAdr>"]
file_pages: [502]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.015.001.04"]
---

# 14.4.3.2.3 CommunicationAddress <ComAdr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 502 to 502.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 502

```text
CodeName Name Definition
transfers ormanagement of standing
instructions for liquidity control.
LMMG LimitManager Party in a financial institution responsible
for the management of the limits. This
party is responsible for fixing, modifying,
or suspending limits as relevant for the
management of counterpart risk or
systemic risk containment.
PYMG PaymentManager Party in a financial institution responsible
for the management of payment
processing for the financial institution.
This includes authorising, recycling, and
modification of payment transactions.
REDR Reader Party in a financial institution entitled to
obtain information from the system, but
not act upon/alter this information.
BKMG BackupManager Party responsible for managing the
recovery functions related to a system.
STMG SettlementManager Party in a financial institution responsible
for the management of settlement
processing.
14.4.3.2.3  CommunicationAddress <ComAdr>
Presence: [1..1]
Definition: Number, or virtual address, used for communication.
CommunicationAddress <ComAdr> contains the following CommunicationAddress8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostalAddress <PstlAdr> [1..1] ± 502
   PhoneNumber <PhneNb> [1..1] Text 503
   FaxNumber <FaxNb> [0..1] Text 503
   EmailAddress <EmailAdr> [0..1] Text 503
14.4.3.2.3.1  PostalAddress <PstlAdr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains one of the following elements (see "LongPostalAddress1Choice"
on page 839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unstructured <Ustrd> [1..1] Text 840
Or}   Structured <Strd> [1..1] ± C3 840
Approved by the Payments SEG on 04 February 2025 camt.015.001.04 ModifyMemberV04
Cash Management - Maintenance 2024 - 2025 502 February 2025
```

