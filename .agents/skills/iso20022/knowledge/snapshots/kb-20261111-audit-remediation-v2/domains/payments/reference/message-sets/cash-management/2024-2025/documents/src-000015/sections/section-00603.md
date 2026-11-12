---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["36 camt.104.001.01 CreateMemberV01", "36.4 Message Building Blocks", "36.4.3 ValueSet <ValSet>", "36.4.3.2 ContactReference <CtctRef>", "36.4.3.2.1 Name <Nm>"]
file_pages: [779]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.104.001.01"]
---

# 36.4.3.2.1 Name <Nm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 779 to 779.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 779

```text
ContactReference <CtctRef> contains the following ContactIdentificationAndAddress1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 779
   Role <Role> [1..1] CodeSet 779
   CommunicationAddress <ComAdr> [1..1]  780
     PostalAddress <PstlAdr> [1..1] ± 780
     PhoneNumber <PhneNb> [1..1] Text 780
     FaxNumber <FaxNb> [0..1] Text 780
     EmailAddress <EmailAdr> [0..1] Text 780
36.4.3.2.1  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max35Text" on page 889
36.4.3.2.2  Role <Role>
Presence: [1..1]
Definition: Role of the party in the activity.
Datatype: "PaymentRole1Code" on page 862
CodeName Name Definition
LQMG LiquidityManager Party in a financial institution responsible
for the management of liquidity for the
financial institution. This party has
access to some functions available on
the system, such as the liquidity
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
Approved by the Payments SEG on 04 February 2025 camt.104.001.01 CreateMemberV01
Cash Management - Maintenance 2024 - 2025 779 February 2025
```

