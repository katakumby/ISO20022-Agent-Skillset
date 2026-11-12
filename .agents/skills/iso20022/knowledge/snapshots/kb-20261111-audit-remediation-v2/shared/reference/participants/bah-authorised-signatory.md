---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
source_ids: ["src-000012"]
source_edition: "Version 3.0, 2021-11-03"
participant_id: "bah-authorised-signatory"
aliases: ["person authorised to sign", "Business Entity authorised to sign", "creator of the Signature"]
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
source_locations: ["§§4.1–4.2.1 pp28–29; §4.2.6 pp31–32; §4.2.10–4.2.11 p33"]
flows: ["bah-signed-message", "bah-signing-business-message", "bah-verifying-signature"]
limitations: ["The authorised person and required signing scenarios are outside the annex scope.", "Historical illustrative MUG profile; not silently applied to supplied V04 schema."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Person or business entity authorised to sign a Business Message

## Definition and role scope

The person or business entity authorised within the applicable business context to sign the entire Business Message. This is a signature-authorisation role; the source does not identify it with a named institution, the transport sender or a universal job title. [§§4.1–4.2.1 pp28–29; §4.2.6 pp31–32; §4.2.10–4.2.11 p33](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Responsibilities and actions

Creates a Signature over the BAH and ISO 20022 Message under agreed signature rules. The guide does not specify who is authorised or which business scenarios must be signed. In the illustrative process the private key signs canonicalized SignedInfo; SignatureValue is calculated as the last creation step. [§§4.1–4.2.1 pp28–29; §4.2.6 pp31–32; §4.2.10–4.2.11 p33](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Identifiers

The illustrative KeyInfo carries an X509v3 certificate containing the validation key. KeyInfo itself has an Id unique within the enclosing XML document. A certificate/key identifies verification material; it is not a universal institutional identifier scheme. [§§4.1–4.2.1 pp28–29; §4.2.6 pp31–32; §4.2.10–4.2.11 p33](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Relationships and applicability

The [bah-signature-verifier](bah-signature-verifier.md) is the counterpart role under the agreed signature structure. [Sending endpoint](bah-sending-messaging-endpoint.md) and [receiving endpoint](bah-receiving-messaging-endpoint.md) are message roles; no equality between those endpoints and the person authorised to sign is asserted. The PKI infrastructure, certification-chain policy and any service/business-area restrictions depend on the implementation context. [§4.1–4.2.1 p28; §4.2.6 pp31–32](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Flows

- [bah-signed-message](../message-sets/business-application-header/2021-11-03-v3.0/flows/signed-message.md).
- [bah-signing-business-message](../message-sets/business-application-header/2021-11-03-v3.0/flows/signing-business-message.md).
- [bah-verifying-signature](../message-sets/business-application-header/2021-11-03-v3.0/flows/verifying-signature.md).

## Evidence and ambiguities

Figure 4 has an apparent reference-connector discrepancy (issue-000017); the source image, textual URI rules and Figure 5 remain separate. [Issue register](../../../tracking/issues.md). This record does not assign authority to a particular person or institution.
