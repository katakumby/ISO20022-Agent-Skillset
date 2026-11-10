---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["14 camt.015.001.04 ModifyMemberV04", "14.4 Message Building Blocks", "14.4.3 NewMemberValueSet <NewMmbValSet>", "14.4.3.2 ContactReference <CtctRef>"]
file_pages: [501]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.015.001.04"]
---

# 14.4.3.2 ContactReference <CtctRef>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 501 to 501.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 501

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 802 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 803
   SchemeName <SchmeNm> [0..1]  803
{Or     Code <Cd> [1..1] CodeSet 803
Or}     Proprietary <Prtry> [1..1] Text 803
   Issuer <Issr> [0..1] Text 803
14.4.3.2  ContactReference <CtctRef>
Presence: [0..*]
Definition: Person to be contacted in a given organisation.
ContactReference <CtctRef> contains the following ContactIdentificationAndAddress1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 501
   Role <Role> [1..1] CodeSet 501
   CommunicationAddress <ComAdr> [1..1]  502
     PostalAddress <PstlAdr> [1..1] ± 502
     PhoneNumber <PhneNb> [1..1] Text 503
     FaxNumber <FaxNb> [0..1] Text 503
     EmailAddress <EmailAdr> [0..1] Text 503
14.4.3.2.1  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max35Text" on page 889
14.4.3.2.2  Role <Role>
Presence: [1..1]
Definition: Role of the party in the activity.
Datatype: "PaymentRole1Code" on page 862
CodeName Name Definition
LQMG LiquidityManager Party in a financial institution responsible
for the management of liquidity for the
financial institution. This party has
access to some functions available on
the system, such as the liquidity
Approved by the Payments SEG on 04 February 2025 camt.015.001.04 ModifyMemberV04
Cash Management - Maintenance 2024 - 2025 501 February 2025
```

