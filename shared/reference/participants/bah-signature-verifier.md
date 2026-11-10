---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
source_ids: ["src-000012"]
source_edition: "Version 3.0, 2021-11-03"
participant_id: "bah-signature-verifier"
aliases: ["verifiers of the Signature", "receiver in the signature-verification example"]
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
source_locations: ["§4.1–4.2 p28; §4.2.2 pp29–30; §4.2.6 pp31–32; §4.2.12 p33; Figure 5 p35"]
flows: ["bah-signed-message", "bah-signing-business-message", "bah-verifying-signature"]
limitations: ["The authorised person and required signing scenarios are outside the annex scope.", "Historical illustrative MUG profile; not silently applied to supplied V04 schema."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Verifier of a BAH Signature

## Definition and role scope

A participant applying the agreed signature structure and verification process to a received Business Message. This functional verification role is scoped to the MUG signature guidelines, not an institution type or proof that every business receiver performs verification itself. [§4.1–4.2 p28; §4.2.2 pp29–30; §4.2.6 pp31–32; §4.2.12 p33; Figure 5 p35](../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf) (src-000012).

## Responsibilities and actions

Reconstructs the defined XML contexts, transforms and digests BAH, ISO message and KeyInfo, compares Reference digests, and verifies SignatureValue using SignedInfo and the certificate/public key. A failed comparison or failed verification produces failure. Agrees the signature structure with the creator. [§4.1–4.2 p28; §4.2.2 pp29–30; §4.2.6 pp31–32; §4.2.12 p33; Figure 5 p35](../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf) (src-000012).

## Identifiers

Uses the X509v3 certificate/public validation key from KeyInfo under the agreed PKI context. The guide does not specify a verifier identifier scheme. [§4.1–4.2 p28; §4.2.2 pp29–30; §4.2.6 pp31–32; §4.2.12 p33; Figure 5 p35](../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf) (src-000012).

## Relationships and applicability

The [bah-authorised-signatory](bah-authorised-signatory.md) is the counterpart role under the agreed signature structure. [Sending endpoint](bah-sending-messaging-endpoint.md) and [receiving endpoint](bah-receiving-messaging-endpoint.md) are message roles; no equality between those endpoints and the person authorised to sign is asserted. The PKI infrastructure, certification-chain policy and any service/business-area restrictions depend on the implementation context. [§4.1–4.2.1 p28; §4.2.6 pp31–32](../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf) (src-000012).

## Flows

- [bah-signed-message](../message-sets/business-application-header/2021-11-03-v3.0/flows/signed-message.md).
- [bah-signing-business-message](../message-sets/business-application-header/2021-11-03-v3.0/flows/signing-business-message.md).
- [bah-verifying-signature](../message-sets/business-application-header/2021-11-03-v3.0/flows/verifying-signature.md).

## Evidence and ambiguities

Figure 4 has an apparent reference-connector discrepancy (issue-000017); the source image, textual URI rules and Figure 5 remain separate. [Issue register](../../../tracking/issues.md). This record does not assign authority to a particular person or institution.
